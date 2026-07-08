# Debugging

*maybe try turning it off and on (again)?*

### is new, wat this?

Basically, I decided that I should probably write down some easy debugging stuff.

### General Tips

- Enable and use force move at the beginning to test out maximum velocity and acceleration configs that you're comfortable with (and the printer is, of course).
- Observe the printer's accuracy and motion (obviously!). It might just be trying to go too fast.

### Mechanical/Config

The belt loop on the tool base collides with the sliders, requiring a huge amount of effort from the motor (which may also push the setup in the x axis when zeroing the y axis).

> Either use double-sided tape and a bunch of tape to secure it against the extruder motor or cut the belts very close if you must (NOT RECOMMENDED).

My belt's skipping/there's some strange clicking noises when I run stuff.

> If it's the coreXY, make sure the belts aren't overtensioned, too loose, and add the top shaft guides (they should be there anyways). In general, make sure that it's not getting caught on anything, and if that still doesn't work, run it on lower speeds and check if that still happens.

It keeps screeching and not moving!

> Try decreasing the velocity and acceleration in the config!

### Tips

Accuracy sucks! It keeps drifting!

> Try lowering the velocity and accelerations and find the fastest/most reliable setup! You're probably aiming to have a reliable and moderately speedy setup rather than a lightning speed unreliable setup.