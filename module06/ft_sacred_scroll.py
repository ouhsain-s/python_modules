import alchemy


def safe_call(func, name):
    result = func()
    print(f"{name}: {result}")


print("=== Sacred Scroll Mastery ===")

print("\nTesting direct module access:")

try:
    safe_call(alchemy.elements.create_fire, "alchemy.elements.create_fire()")
    safe_call(alchemy.elements.create_water, "alchemy.elements.create_water()")
    safe_call(alchemy.elements.create_earth, "alchemy.elements.create_earth()")
    safe_call(alchemy.elements.create_air, "alchemy.elements.create_air()")
except AttributeError:
    print("AttributeError - not exposed")

print("\nTesting package-level access (controlled by __init__.py):")

try:
    safe_call(alchemy.create_fire, "alchemy.create_fire()")
    safe_call(alchemy.create_water, "alchemy.create_water()")
except ArithmeticError:
    print("AttributeError - not exposed")

try:
    safe_call(alchemy.create_earth, "alchemy.create_earth()")
except AttributeError:
    print("alchemy.create_earth(): AttributeError - not exposed")

try:
    safe_call(alchemy.create_air, "alchemy.create_air()")
except AttributeError:
    print("alchemy.create_air(): AttributeError - not exposed")

print("\nPackage metadata:")

print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")
