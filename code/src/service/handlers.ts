function areEqualDates(dateLeft: Date, dateRigth: Date) {
  if (dateLeft > dateRigth) {
    return false;
  } else if (dateLeft < dateRigth) {
    return false;
  } else {
    return true;
  }
}

export { areEqualDates };
