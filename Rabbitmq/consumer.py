try:
    import pika
except Exception as e:
    print("there is an error.")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()
channel.queue_declare(queue='IntQueue')
def callback(ch,method,properities,body):
    # print(" [x] Received %r" % body)
    # print(" [x] Received " ,body[0])
    # print(" [x] Received %r" %body)
    # comming_message = str(body).strip(',')
    comming_message = str(body).strip()
    print("comming numbers: ",comming_message)
    # print("comming_message: ",comming_message)
    num_1 =  int(comming_message[2])
    num_2 =  int(comming_message[3])

    # print(" Received Message: ",comming_message + ' manzoor')
    print("The Multiplication of  :",num_1, 'and', num_2, ' is: ',num_1 * num_2) 
    print("."*50,'\n')
    # print(type(body))

    # print(" [x] Received %r" %body.split(','))

channel.basic_consume(
    queue='IntQueue',on_message_callback=callback,auto_ack=True
)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()