class IcoData:

    def __init__(self,type,name,startDate,endDate):
        self.name = name
        self.type = type
        self.startDate = startDate
        self.endDate = endDate

    def __str__(self):
        return 'icodata (name=%s) (type=%s) (startDate=%s) (endDate=%s)' %(self.name, self.type.value, self.startDate, self.endDate)
