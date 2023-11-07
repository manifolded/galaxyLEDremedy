import time
import random

num_pixels = 300

ave_interval = 2
ave_duration = 0.1
ave_brightness = 50.0

max_stars = 100
current_stars = []

def define_star():
    inception_time = time.time()+random.expovariate(ave_interval)
    destruction_time = inception_time+random.expovariate(ave_duration)
    brightness = random.randint(0, 2*ave_brightness)
    if brightness > 255:
        brightness = 255
    return {
        'pixel_index': random.randint(0, 255),
        'brightness': brightness,
        'inception_time': inception_time,
        'destruction_time': destruction_time,
        'instantiated': False
    }

# define_star() must be called before instantiate_star()
def instantiate_star(new_star, my_strip):
    my_strip[new_star['pixel_index']] = (
        new_star['brightness'],
        new_star['brightness'],
        new_star['brightness']
    )
    my_strip.show()
    new_star['instantiated'] = True

def testForInstantiation(new_star):
    return time.time() >= new_star['inception_time'] and not new_star['instantiated']

def destroy_stars(current_stars, my_strip):
    for star in current_stars:
        if time.time() > star['destruction_time']:
            my_strip[star['pixel_index']] = (0,0,0)
            my_strip.show()
            current_stars.remove(star)
            # lastly, everytime you destroy a star you create a new one.
            # Must be done here since here we can replace them
            replacement_star = define_star()
            current_stars.append(replacement_star)
            # leave this star to be initialized on the next event loop iteration

# initialize stars
for star_count in range(0, max_stars):
    new_star = define_star()
    current_stars.append(new_star)
    # Don't instantiate stars until looping.
    # if testForInstantiation(new_star):
    #     instantiate_star(new_star, my_strip)

# evolve stars
def iteration(my_strip):
    global current_stars
    # Check if new_star is ready yet and if so instantiate
    for star in current_stars:
        if testForInstantiation(star):
            instantiate_star(star, my_strip)
    # Clean up any expired stars
    destroy_stars(current_stars)


