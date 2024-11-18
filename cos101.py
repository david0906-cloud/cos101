def calculate_velocity():

    displacement=float(input('displacement'))

    time=float(input("time"))

    velocity=displacement / time
    print('velocity is',velocity)
calculate_velocity()

def calculate_force():

    mass=float(input("mass"))

    acceleration=float(input("acceleration"))

    force=mass*acceleration
    print("force is ",force)
calculate_force()

def calculate_power():

    work=float(input("work"))

    time=float(input("time"))

    power=work/time
    print('power is',power)
calculate_power()

def calculate_pressure():

    force=float(input("force"))

    area=float(input('area'))

    pressure=force/area
    print('pressure is',pressure)
calculate_pressure()

def calculate_density():

    mass=float(input("mass"))

    volume=float(input("volume"))

    density=mass*volume
    print("density is",density)
calculate_density()