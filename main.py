# function to current date and time
def current_date_time():
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


# Main function

if __name__ == '__main__':
    print(current_date_time())
    print("hello")

#test




