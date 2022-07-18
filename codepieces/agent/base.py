from common.registry import Registry


# @Registry.register_model('base')
class BaseAgent(object):
    '''
    BaseAgent
    '''
    def __init__(self, world):
        '''
        __init__
        :param world:
        '''
        # revise if it is multi-agents in one model
        self.world = world
        self.sub_agents = 1

    def get_ob(self):
        '''
        get_ob

        :return:
        '''
        raise NotImplementedError()

    def get_reward(self):
        '''
        get_reward
        :return:
        '''
        raise NotImplementedError()

    def get_action(self, ob, phase):
        '''get_action

        :param ob:
        :param phase:
        :return:
        '''
        raise NotImplementedError()
