<?php
namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Models\User;
use Illuminate\Support\Facades\Hash;
use Illuminate\Validation\ValidationException;

class AuthController extends Controller
{
    // Register a new user
    public function register(Request $request)
    {
        try{
            $request->validate([
                'name' => 'required|string|max:255',
                'email' => 'required|string|email|max:255|unique:users',
                'password' => 'required|string|min:8|confirmed',
            ]);
            $user = User::create([
                'name' => $request->name,
                'email' => $request->email,
                'password' => Hash::make($request->password),
            ]);
            return response()->json(['message' => 'User registered successfully'], 201);
        }catch (\Exception $ex) {
            return response()->json(null, 204);
        }
    }

    // Log in a user and return a token
    public function login(Request $request)
    {
        try{
            $request->validate([
                'email' => 'required|string|email',
                'password' => 'required|string',
            ]);

            $user = User::where('email', $request->email)->first();

            if (!$user || !Hash::check($request->password, $user->password)) {
                throw ValidationException::withMessages([
                    'email' => ['The provided credentials are incorrect.'],
                ]);
            }
            $token = $user->createToken('auth_token')->plainTextToken;
            return response()->json(['token' => $token], 200);
        }catch (\Exception $ex) {
            return response()->json(null, 204);
        }
    }

    // Log out a user and revoke the token
    public function logout(Request $request)
    {
        try{
            $request->user()->currentAccessToken()->delete();
            return response()->json(['message' => 'Logged out successfully'], 200);
        }catch (\Exception $ex) {
            return response()->json(null, 204);
        }
    }


    // Get user Dat
    public function getUser(Request $request)
    {
        try{
            $user = $request->user();
            return response()->json(['data' => $user], 200);
        }catch (\Exception $ex) {
            return response()->json(null, 204);
        }
    }
}