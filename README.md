# A Strategy for completing CommonRoad Prize Challenge

## Notes

- *student.py* is just an initial version, but it still can solve more than 350 scenarios out of the 500 scenerios given by the CommonRoad task.
- the final code based on this strategy solves more than 1300 scenarios out of 2000 scenarios given by the CommonRoad Prize Challenge and gets the top 10 in the competition
- due to the deadline of the competition, the code wasn't be polished perfectly, so the performance could be much better.

## The outline of the strategy
- the basic idea is exploiting the **RoutePlanner** function to get the optimal route, which will be followed by the vehicle.
- there are some important parameters considered: 
  - the distance between current position and the goal position(if the goal position is an interval or point instead of a lanet id)
  - the distance between current position and the reference path given by the **RoutePlanner** funtion
  - the difference between
