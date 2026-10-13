import math
import csv
import matplotlib.pyplot as plt


print("=" * 55)
print("          ROCKET PERFORMANCE CALCULATOR")
print("=" * 55)
print("Ideal rocket performance analysis tool")
print("Calculates propulsion and mass-performance parameters")
print("=" * 57)

# rocket inputs
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a value greater than zero.")
            else: 
                return value
        except ValueError:
            print("Please enter valid number.")
                    
thrust = get_positive_float("Enter thrust (N): ")
mass_flow_rate = get_positive_float("Enter mass fow rate (kg/s): ")
propellant_mass = get_positive_float("Enter propellant mass (kg): ")
dry_mass = get_positive_float("Enter dry mass (kg): ")

def calculate_exhaust_velocity(thrust, mass_flow_rate):
    return thrust / mass_flow_rate

def calculate_specific_impulse(exhaust_velocity):
    return exhaust_velocity / G0

def calculate_mass_ratio(initial_mass, final_mass):
    return initial_mass / final_mass

def calculate_delta_v(exhaust_velocity, mass_ratio):
    return exhaust_velocity * math.log(mass_ratio)

# Exhaust velocity

exhaust_velocity = calculate_exhaust_velocity(thrust, mass_flow_rate)
print(f"\nExhaust velocity: {exhaust_velocity:.2f} m/s")

# specific impulse

G0 = 9.80665

specific_impulse = calculate_specific_impulse(exhaust_velocity)
print(f"Specific impulse: {specific_impulse:.2f} s")

# exhaust velocity consistency check

calculated_exhaust_velocity = specific_impulse * G0
print(f"Calculated exhaust velocity: {calculated_exhaust_velocity:.2f}%")
# mass ratio

initial_mass = propellant_mass + dry_mass
final_mass = dry_mass

mass_ratio = calculate_mass_ratio(initial_mass, final_mass)
print(f"Mass ratio: {mass_ratio:.2f}")

# propelant mass fraction

propellant_mass_fraction = propellant_mass / initial_mass
propellant_percentage = propellant_mass_fraction * 100

print(f"Propellant mass fraction: {propellant_mass_fraction:.3f}")
print(f"Propellant percentage:     {propellant_percentage:.2f}%")

# delta-v

delta_v = calculate_delta_v(exhaust_velocity, mass_ratio)
print(f"Delta-v: {delta_v:.2f} m/s")

# thrust - weight ratio

thrust_to_weight = thrust / (initial_mass * G0)
print(f"Thrust to weight ratio: {thrust_to_weight:.2f}")
if thrust_to_weight < 1 :
    print("WARNING: Thrust to weight ratio is below 1.")
    print("The rocket may not be able to lift off vertically.")
else:
    print("Thrust to weight ratio is sufficient for liftoff.")

# burn time

burn_time = propellant_mass / mass_flow_rate
print(f"Burn time:    {burn_time:.2f} s")

# result 

print("\n" + "=" * 50)
print("ROCKET PERFORMANCE RESULTS")
print("=" * 50)

print(f"Initial mass:          {initial_mass:.2f} kg")
print(f"Final mass:            {final_mass:.2f} kg")
print(f"Propellant mass:       {propellant_mass:.2f} kg")
print(f"Propellant mass fraction:   {propellant_mass_fraction:.2f}%")
print("=" * 50)
print(f"Mass ratio:            {mass_ratio:.2f}")
print(f"Exhaust velocity:      {exhaust_velocity:.2f} m/s")
print(f"Specific impulse:      {specific_impulse:.2f} s")
print(f"Delta-v:               {delta_v:.2f} m/s")
print(f"Thrust to weight ratio:  {thrust_to_weight:.2f}")
print(f"Burn time:                {burn_time:.2f} s")
print("=" * 50)

# performance assesment

print("\n" + "=" * 50)
print("PERFORMANCE ASSESMENT")
print("=" * 50)

if specific_impulse >= 300:
    print("Specific impulse: High")
elif specific_impulse >= 200:
    print("Specific impulse: Moderate")
else:
    print("Specific impulse: Low")

if thrust_to_weight > 1:
    print("Liftoff capability: PASS")
else:
    print("Liftoff capability: FAIL")

if propellant_percentage >= 70:
    print("Propellant fraction: High")
elif propellant_percentage >= 50:
    print("Propellant fraction: Moderate")
else: 
    print("Propellant fraction: Low")

print("=" * 50)

# delta-v validation

delta_v_from_isp = specific_impulse * G0 * math.log(mass_ratio)
difference = abs(delta_v - delta_v_from_isp)

print("\n" + "=" * 50)
print("DELTA-V VALIDATION")
print("=" * 50)

print(f"Delta-v from exhaust velocity:  {delta_v:.2f} m/s")
print(f"Delta-v from Specific impulse:   {delta_v_from_isp:.2f} m/s")
print(f"Difference:  {difference:.6f} m/s")

if difference < 0.01:
    print("Validation: PASS")
else: 
    print("Validation: CHECK CALCULATONS")

print("=" * 50)

# propellant mass sensitivity study

propellant_masses = []
delta_v_values = []

print("\n" + "=" * 45)
print("PROPELLANT MASS vs DELATA-V")
print("=" * 45)

for prop_mass in range(100, 1001, 100):
    test_initial_mass = prop_mass + dry_mass
    test_mass_ratio = test_initial_mass / dry_mass
    test_delta_v = exhaust_velocity *  math.log(test_mass_ratio)

    propellant_masses.append(prop_mass)
    delta_v_values.append(test_delta_v)

    print(
        f"Propellant:   {prop_mass:4d} kg| "
        f"Delta-v:      {test_delta_v:8.2f} m/s"
    )

# plot

import matplotlib.pyplot as plt
plt.plot(propellant_masses, delta_v_values, marker="o")
plt.xlabel("Propellant Mass (Kg)")
plt.ylabel("Delta-v (m/s)")
plt.title("Delta-v vs Propellant Mass")
plt.grid(True)
plt.show()

# Exhaust velocity sensitivity study

exhaust_velocities = []
delta_v_exhaust = []

print("\n" + "=" * 45)
print("EXHAUST VELOCITY vs DELTA-V")
print("=" * 45)

for velocity in range(1500, 4001, 250):
    test_delta_v = velocity * math.log(mass_ratio)

    exhaust_velocities.append(velocity)
    delta_v_exhaust.append(test_delta_v)
    print(
        f"Exhaust velocity:  {velocity:4d} m/s | "
        f"Delta-v:           {test_delta_v:8.2f} m/s"
    )

plt.figure()
plt.plot(exhaust_velocities, delta_v_exhaust, marker="o")

plt.xlabel("Exhaust Velocity (m/s)")
plt.ylabel("Delta-v (m/s)")
plt.title("Delta-v vs Exhaust Velocity")

plt.grid(True)
plt.show()

#Export propellant sensitivity results to CSV
import csv

with open("rocket_performance_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Propellant Mass (Kg)", "Delta-v (m/s)"])
    for prop_mass, dv in zip(propellant_masses, delta_v_values):
        writer.writerow([prop_mass, dv])

print("\nResults saved to rocket_performance_results.csv")   

# rocket configuraton comparison

configurations = {
    "Light": 300,
    "Medium": 500,
    "Heavy": 700
}
print("\n" + "=" * 50)
print("ROCKET CONFIGURATION COMPARISON")
print("=" * 50)

for name, prop_mass in configurations.items():
    config_initial_mass = prop_mass + dry_mass
    config_mass_ratio = config_initial_mass / dry_mass
    config_delta_v = exhaust_velocity * math.log(config_mass_ratio)

    print(
        f"{name:8} | "
        f"Propellant: {prop_mass:4d} kg | "
        f"Delta-v: {config_delta_v:8.2f} m/s"
    )
print("=" * 50)

config_names = []
config_delta_v_values = []

for name, prop_mass in configurations.items():
    config_initial_mass = prop_mass + dry_mass
    config_mass_ratio = config_initial_mass / dry_mass
    config_delta_v = exhaust_velocity * math.log(config_mass_ratio)

    config_names.append(name)
    config_delta_v_values.append(test_delta_v)

plt.figure()
plt.bar(config_names, config_delta_v_values)

plt.xlabel("Rocket Configuration")
plt.ylabel("Delta-v (m/s)")
plt.title("Delta-v comparison")

plt.grid(axis="y")
plt.show()






