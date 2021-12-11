import time
import random
count_message = 1
while True:
    try:
        import pika
    except Exception as e:
        print("There  is an error:  {}".format(e))
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    channel.queue_declare(queue='IntQueue')
    random_int = [random.randint(0,10) for _ in range(2)]

    message = ''.join(map(str, random_int))
    channel.basic_publish(exchange='', routing_key='IntQueue', body=message)

    print("Published Message ",count_message)
    count_message+=1
    connection.close()
    time.sleep(2)
