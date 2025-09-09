#height of falling ball function
def calculate_height(h0, t):
    g=9.8
    return h0 - 0.5 * g * t * t

#User inputs height and time:
height=float(input("enter height initial"))
time=float(input("Enter time:"))
print(f"The height of the ball at {time} s is {calculate_height(height, time)} meters")

height=float(input("Enter Height initial:"))
time=float(input("Enter time:"))
print(f"The height of the ball at {time} s is {calculate_height(height, time)} meters")

height=float(input("Enter Height initial:"))
time=float(input("Enter time:"))
print(f"The height of the ball at {time} s is {calculate_height(height, time)} meters")

#Car distance function
def car_distance_calculation(t):
    speed=5
    return t*speed

#User inputs time
time=float(input("Enter the amount of time the car will be travelling:"))
print(f"The car will be travelling for {car_distance_calculation(time)} m in {time} seconds")

time=float(input("Enter the amount of time the car will be travelling:"))
print(f"The car will be travelling for {car_distance_calculation(time)} m in {time} seconds")

time=float(input("Enter the amount of time the car will be travelling:"))
print(f"The car will be travelling for {car_distance_calculation(time)} m in {time} seconds")
