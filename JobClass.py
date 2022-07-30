

#Creates Job() class, which keeps track of:
# Job Name
# Job Wage
# Pay Frequency
# Hours per average pay period
# Benefit deductions

class Job():

    def __init__(self, name = "Not Specified", wage = 0, payFreq = 0, avgHours = 0, deductions = 0, notes = 0):
        self.name = name
        self.wage = wage
        self.payFreq = payFreq
        self.avgHours = avgHours
        self.deductions = deductions
        self.notes = notes

    def __repr__(self):
        msg = """
        {name} | ${wage}/hr, Pay Frequency: {payFreq}, Average hours per pay period: {avgHours}, Deduction amount: {deductions}, Notes: {notes}
        """.format(name=self.name, wage=self.wage, payFreq=self.payFreq, avgHours=self.avgHours, deductions=self.deductions, notes=self.notes)

    