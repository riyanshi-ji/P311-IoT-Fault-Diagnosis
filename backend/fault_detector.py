def diagnose_fault(temperature, vibration, current):

    faults = []

    if temperature > 85:
        faults.append("High Temperature")

    if vibration > 70:
        faults.append("Excessive Vibration")

    if current > 8:
        faults.append("High Current")

    if len(faults) == 0:
        status = "NORMAL"
    elif len(faults) == 1:
        status = "WARNING"
    else:
        status = "CRITICAL"

    return status, faults