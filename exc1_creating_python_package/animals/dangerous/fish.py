class Fish:
    '''
    '''

    def __init__(self):
        '''
        '''
        self.members = ['Shark', 'Cod', 'Hering']
    
    def printMembers(self):
        '''
        '''
        print('The members of the class "Fish" are:')
        for member in self.members:
            print('\t %s' %member)
