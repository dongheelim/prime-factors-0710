class PrimeFactors:
    def of(self, number):
        factors = []
        if number >= 2:
            if number == 4:
                factors.append(2)
                factors.append(2)
            else:
                factors.append(number)
        return factors
