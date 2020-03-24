class Birds:
    '''
    '''

    def __init__(self):
        """
        """
        self.members = ['Seagull', 'Dove', 'Raven']


    def printMembers(self):
        '''
        '''
        print('The members of the class "Birds" are:')
        for member in self.members:
            print('\t %s' %member)
