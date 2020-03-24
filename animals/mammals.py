class Mammals:
    '''
    '''

    def __init__(self):
        '''
        '''
        self.members = ['Dolphin', 'Whale', 'Elephant']
    
    def printMembers(self):
        '''
        '''
        print('The members of the class "Mammals" are:')
        for member in self.members:
            print('\t %s' %member)
