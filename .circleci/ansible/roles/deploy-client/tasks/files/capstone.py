import requests
import datetime

today = datetime.datetime.now()
date_time = today.strftime("%m/%d/%Y, %H:%M:%S")


def is_hellow_up(date_time):
    try:
        response = requests.get('a4938475e3c9a4f0fb580bf5a5cf8163-873477052.us-west-2.elb.amazonaws.com')
        #print('Server up', date_time)
        print('HTTP Code:',response.status_code)
        log = open\
            ('/Users/i859241/Dropbox/Github/udacity/udacity_capstone/.circleci/ansible/roles/deploy-client/tasks/files/\
            log.txt', 'a')
        log.write(f'{date_time} Hellow World UP')
        log.close()
    except:
        ##print(date_time)
        #print('Server down')
        log = open\
            ('/Users/i859241/Dropbox/Github/udacity/udacity_capstone/.circleci/ansible/roles/deploy-client/tasks/files/\
            log.txt', 'a')
        log.write(f'{date_time} Hellow World DOWN')
        log.close()
def main():
    is_hellow_up(date_time)

if __name__ == "__main__":
    main()

