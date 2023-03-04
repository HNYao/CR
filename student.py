import numpy as np

from SMP.motion_planner.node import PriorityNode

from SMP.motion_planner.plot_config import DefaultPlotConfig
from SMP.motion_planner.search_algorithms.best_first_search import GreedyBestFirstSearch

from commonroad_route_planner.route_planner import RoutePlanner

class StudentMotionPlanner(GreedyBestFirstSearch):
    """
    Motion planner implementation by students.
    Note that you may inherit from any given motion planner as you wish, or come up with your own planner.
    Here as an example, the planner is inherited from the GreedyBestFirstSearch planner.
    """

    def __init__(self, scenario, planningProblem, automata, plot_config=DefaultPlotConfig):
        super().__init__(scenario=scenario, planningProblem=planningProblem, automaton=automata,
                         plot_config=plot_config)

        #use route_planner to get the reference route
        self.route_planner = RoutePlanner(scenario = scenario,
                                          planning_problem=planningProblem,
                                          )

        self.route_ref = self.route_planner.plan_routes().retrieve_best_route_by_orientation().reference_path






    def evaluation_function(self, node_current: PriorityNode) -> float:
        ########################################################################
        # todo: Implement your own evaluation function here.                   #
        ########################################################################
        node_current.priority = self.heuristic_function(node_current)
        return node_current.priority

    def heuristic_function(self, node_current: PriorityNode) -> float:
        ########################################################################
        # todo: Implement your own heuristic cost calculation here.            #
        # Hint:                                                                #
        #   Use the State of the current node and the information from the     #
        #   planning problem, as well as from the scenario.                    #
        #   Some helper functions for your convenience can be found in         #
        #   ./search_algorithms/base_class.py                             #
        ########################################################################


        # 01 get the current state
        path_last = node_current.list_paths[-1] #get the path
        pos_current = path_last[-1].position #get the current position
        time_step_current = path_last[-1].time_step #get the current timestep
        vel_current = path_last[-1].velocity #get the current velocity
        ori_current = path_last[-1].orientation #get the current orientation

        if time_step_current > self.time_desired.end: #timeout
            return np.inf

        # 02 the distance from car to goal
        if self.position_desired is not None:
            dis_goal = self.calc_euclidean_distance(node_current)
        else:
            return self.myheuristic(node_current)

        # 03 the distance from car to the referecne path
        len_route_ref = len(self.route_ref)
        index_route_ref = int((time_step_current / self.time_desired.end) * len_route_ref) - 1
        dis_route_ref = self.myeuclidean(pos_current, self.route_ref[index_route_ref])

        # 04 velocity
        if self.position_desired is not None:
            vel_ref = dis_goal / (self.time_desired.end - time_step_current + 0.1)
            dif_vel = abs(vel_ref - vel_current)
        else:
            dif_vel = 0

        return 1 * dis_goal + 1* dis_route_ref + 1 * dif_vel


    def myeuclidean(self, pos_1, pos_2) -> float :
        """
        input 2 positions
        Returens the euclidean distance between 2 positions
        """

        dis = np.sqrt(pow(pos_1[0] - pos_2[0],2) + pow(pos_1[1] - pos_2[1],2))

        return dis


    def myheuristic(self, node_current):
        if self.reached_goal(node_current.list_paths[-1]):
            return 0.0

        if self.position_desired is None:
            return self.time_desired.start - node_current.list_paths[-1][-1].time_step

        else:
            velocity = node_current.list_paths[-1][-1].velocity

            if np.isclose(velocity, 0):
                return np.inf

            else:
                return self.calc_euclidean_distance(current_node=node_current) / velocity







