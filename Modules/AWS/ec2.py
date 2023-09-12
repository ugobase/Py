def create_ec2_instance(ami, key_pair, instance_type):
    print("Creating ec2 instance with: ",ami,key_pair,instance_type)


def stop_instance(instance_id):
    print("stopping the instance with id: ", instance_id)

def insert_user_info(name, email, password):
    print("inserting user details in db: ", name,email,password)