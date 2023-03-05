# A Strategy for completing CommonRoad Prize Challenge

## Notes

- *student.py* is just an initial version, but it still can solve more than 350 scenarios out of the 500 scenarios given by the CommonRoad task.
- the final code based on this strategy solves more than 1300 scenarios out of 2000 scenarios given by the CommonRoad Prize Challenge and gets the top 10 in the competition
- due to the deadline of the competition, the code wasn't be polished perfectly, so the performance could be much better.

## The outline of the strategy
- the basic idea is exploiting the **RoutePlanner** function to get the optimal route, which will be followed by the vehicle.
- there are some important parameters considered: 
  - the distance between current position and the goal position(if the goal position is an interval or point instead of a lane id)
  - the distance between current position and the reference path given by the **RoutePlanner** function
  - the difference between the current orientation and the reference orientation
  - the difference between the current velocity and the reference velocity

## The cost function
In the CommonRoad competition, a **[cost function](https://gitlab.lrz.de/tum-cps/commonroad-cost-functions/-/blob/master/costFunctions_commonRoad.pdf)** is given. Less change in velocity and orientation will lead to a higher performance given the cost function. There are 2 reasonable methods:
- Use the primitives which has less branch so that the vehicle will not always change the orientation and velocity 
- add penalty term related to the change in velocity and orientation

## Primitives



