import requests

def is_hellow_up():
    try:
        response = requests.get('http://localhost')
        print('Server up')
        print('HTTP Code:',response.status_code)
    except:
        print('Server down')

def main():
    is_hellow_up()

if __name__ == "__main__":
    main()

