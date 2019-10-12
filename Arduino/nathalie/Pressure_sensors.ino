int pressure_sensing(int pressure_pin){
   int pressure_value     = analogRead(pressure_pin); 
   /*
   int value_of_voltage   = double(((pressure_value*used_voltage)) / 1023);
   int value_of_newton    = convert_to_newtons(value_of_voltage); 
   */
   
   prev_value = pressure_value;
   
   return (pressure_value);
}

int mapping_val(int press_val, String placement){
  int val = 0;
  if (placement.equals("LEFT")){
    val = map(press_val, 0, HIGH_left, 0, 100);
    return val;
  }
  else if (placement.equals("RIGHT")){
    val = map(press_val, 0, HIGH_right, 0, 100);
    return val;
  }
  return val;
}


double convert_to_newtons()
{
  /* General fitting model Exp2:
     f(x) = a*exp(b*x) + c*exp(d*x)
     Coefficients (with 95% confidence bounds):
       a =     0.01419  (0.01163, 0.01676)
       b =      0.9523  (0.8922, 1.012)
       c =    -0.01461  (-0.02317, -0.006043)
       d =      -2.231  (-6.605, 2.142)
       Goodness of fit:
       SSE: 7.906e-06
       R-square: 0.9999
       Adjusted R-square: 0.9997
       RMSE: 0.001988
   */
   double a = 0.01419 ;
   double b = 0.9523;
   double c = -0.01461;
   double d = -2.231;
    
  return( (a*exp(b*used_voltage) + c*exp(d*used_voltage)) * 9.81 ); // the result of the fit is in KgF to convert to newton we simply
                                                      // multiply by 9.81, if you want data in KgF, remove the final multiplication!
}
