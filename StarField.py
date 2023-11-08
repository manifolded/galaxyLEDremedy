import time
import random

class Stars:

    def __init__(self) -> None:
        self.num_pixels = 300

        self.ave_interval = 2
        self.ave_duration = 0.1
        self.ave_brightness = 50.0

        self.max_stars = 100
        self.current_stars = []

        # initialize first stars
        for _ in range(0, self.max_stars):
            new_star = self.define_star()
            self.current_stars.append(new_star)


    def define_star(self):
        inception_time = time.time()+random.expovariate(self.ave_interval)
        destruction_time = inception_time+random.expovariate(self.ave_duration)
        brightness = random.randint(0, 2*self.ave_brightness)
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
    def instantiate_star(self, new_star, my_strip):
        # Wait, this is no longer allowed. But without it the function is NULL. Add to to-do list.
        my_strip[new_star['pixel_index']] = (
            new_star['brightness'],
            new_star['brightness'],
            new_star['brightness']
        )
        new_star['instantiated'] = True

    def testForInstantiation(self, new_star):
        return time.time() >= new_star['inception_time'] and not new_star['instantiated']

    def remove_stars(self, my_strip):
        for star in self.current_stars:
            if time.time() > star['destruction_time']:
                my_strip[star['pixel index']] = (0,0,0)
                self.current_stars.remove(star)

                # lastly, everytime you destroy a star you create a new one.
                # Must be done here since here we can replace them
                replacement_star = self.define_star()
                self.current_stars.append(replacement_star)
                # leave this star to be initialized on the next event loop iteration



    # evolve stars
    def iteration(self, my_strip):
        # Check if new_star is ready yet and if so instantiate
        for star in self.current_stars:
            if self.testForInstantiation(star):
                self.instantiate_star(star, my_strip)
        # Clean up any expired stars
        self.remove_stars()
        my_strip.show()

