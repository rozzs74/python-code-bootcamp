# Description: Program that computes the volume of the sphere
# Author: John Royce Punay
# Date created: March 3, 2018 9:30PM
# 4(3.14)(r3) / 3 formula for getting the volume of sphere

def get_volume_sphere(radius):
    pi_value = 3.14
    sphere_volume = ((4 * pi_value) * (int(radius) ** 3)) / 3
    formatted_value = format(sphere_volume, '.5f')
    print(formatted_value)

def main():
    print("<----- Calculate the volume of sphere ---->")
    while True:
        try:
            radius_value = float(input("Enter radius value: "))
            get_volume_sphere(radius_value)
            break
        except:
            ValueError
            print('Invalid radius values please enter number!')
            continue    
main()



    

