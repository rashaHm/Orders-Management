# Orders Management
 
# Laravel App
You can register and login using (/login , /register ) paths. I have used laravel
sanctum to implement the authentication. And I have provide logout route.
When user logged in using bearer token he can add order by enter
(customer_name, email, product,status).
There is an api resources to apply (crud) on order, laravel app works on port 8000.
To detect fraud the system sends a request by using api (‘/detect-orderfraud/{order_id}’/), the system will find order by id then use the past fraud history
from payload, after that send request to Django app after getting the result the
system see if the score is bigger than 80 the stauts of order will be change to
‘reject‘, if the score is smaller than 30 the status will be ‘approved’ , otherwise it is
‘pendding’ then apply save on order.

# Django app
There is an api (‘detect- fraud’), we send (order amount , customer email domain,
and past fraud history) data in payload then we get the score , I have run Django
project on port 7000.
I have created a dummy dataset contains 1000 rows and the columns are
(order_amount, email_domain, past_fraud_history, is_fraud).
I have used the Random Forest Classifier to train the model.
