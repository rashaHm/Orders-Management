<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Order;
use GuzzleHttp\Client;
use GuzzleHttp\Exception\RequestException;
class OrderController extends Controller
{

    public function index(Request $request)
    {
        $orders = Order::all();
        return response()->json(['data' => $orders], 200);
    }

    public function create()
    {
        //
    }

    public function store(Request $request)
    {
        try{
            $params = $request->all();
            $request->validate([
                'customer_name' => 'required|string|max:255',
                'email' => 'required|string|email',
                'product' => 'required|string|max:255',
                'amount' => 'required|numeric|between:0,1000',
            ]);

            $order = Order::create([
                'customer_name' => $params['customer_name'],
                'email' => $params['email'],
                'product' => $params['product'],
                'amount' => $params['amount'],
                'status' => $params['status'],
            ]);
            return response()->json(['data' => $order], 200);
        }catch (\Exception $ex) {
            return response()->json(null, 200);
        }
    }

    public function show($id)
    {
        $order = Order::where('id', $id)->first();
        return response()->json(['data' => $order], 200);
    }

    public function edit(Ordereur $Ordereur)
    {
        //
    }

    public function update(Request $request)
    {
        try{
            $order = Order::where('id', $request->id)->first();
            if( $request->customer_name) $order->customer_name = $request->customer_name;
            if( $request->email) $order->email = $request->email;


            if( $request->product) $order->product = $request->product;

            if( $request->amount) $order->amount = $request->amount;


            if( $request->status) $order->status = $request->status;
 
            $order->save();
            return response()->json(['data' => $order], 200);
        }catch (\Exception $ex) {
            return response()->json(null, 200);
        }
    }

    public function destroy($id)
    {
        try {
            $order = Order::where('id', $id)->first();        
            $order->delete();
        } catch (\Exception $ex) {
            return response()->json(null, 204);
        }
        return response()->json(['data' => 'Order is deleted successfully'], 200);
    }

    function detectOrderFraud($id,Request $request) {
        
        try{
            $order = Order::where('id', $id)->first();
            $orderAmount = $order->amount;
            $emailDomain = explode('@', $order->email);
            $pastFraudHistory = $request->past_fraud_history;
            $client = new Client();
            
            $response = $client->post('http://127.0.0.1:7000/api/detect-fraud/', [
            "json"=>  [
                    'order_amount' => $orderAmount,
                    'email_domain' => (string)$emailDomain[1],
                    'past_fraud_history' => $pastFraudHistory,
                ],
            ]);
           
            
         
        
            $data= json_decode($response->getBody(), true);
            $fraudScore = $data['fraud_score'][0];
            if ($fraudScore > 80) {
                $order->status = 'Rejected';
            } elseif ($fraudScore < 30) {
                $order->status = 'Approved';
            } else {
                $order->status = 'Pending';
            }
            $order->save();
            return $order;

        
        } catch (RequestException $e) {
            // Handle exception
            echo $e->getMessage();
            if ($e->hasResponse()) {
                echo $e->getResponse()->getBody()->getContents();
            }
        }
    }
}
