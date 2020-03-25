void mspCom(roll, pitch, yaw, throttle) {
  // msp_attitude_t attitude;
  msp_raw_imu_t imu; 
  msp_altitude_t altitude;
  msp_set_raw_rc_t rc;
  
  msp.command(MSP_SET_RAW_RC, &rc, sizeof(rc), false);

  /*
  if (msp.request(MSP_ATTITUDE, &attitude, sizeof(attitude))) {
    int16_t roll     = attitude.roll;
    int16_t pitch    = attitude.pitch;
    uint16_t yaw     = attitude.yaw;
    Serial.println("Att-Roll: " + String(roll/10.0));
    Serial.println("Att-Pitch: " + String(pitch/10.0));
    Serial.println("Att-Yaw: " + String(yaw));
  }
  */
  
  if (msp.request(MSP_RAW_IMU, &imu, sizeof(imu))) {
    uint16_t acc_x     = imu.acc[0];
    uint16_t acc_y     = imu.acc[1];
    uint16_t acc_z     = imu.acc[2];
    uint16_t gyro_x    = imu.gyro[0];
    uint16_t gyro_y    = imu.gyro[1];
    uint16_t gyro_z    = imu.gyro[2];
    uint16_t mag_x     = imu.mag[0];
    uint16_t mag_y     = imu.mag[1];
    uint16_t mag_z     = imu.mag[2];
  Serial.println("Accelerometer[x,y,z]: " + String(acc_x/448)+ ","+ String(acc_y/448) +","+ String(acc_z/448));
  Serial.println("Gyroscope[x,y,z]: " + String(gyro_x/2000)+ ","+ String(gyro_y/2000) +","+ String(gyro_z/2000));
  Serial.println("Magnetometer[x,y,z]: " + String(mag_x)+ ","+ String(mag_y) +","+ String(mag_z));
  }
  if (msp.request(MSP_ALTITUDE, &altitude, sizeof(altitude))) {
    // int32_t alt_est  = altitude.estimatedActualPosition;  // cm
    // int16_t vel_est  = altitude.estimatedActualVelocity;  // cm/s
    int32_t bara_alt = altitude.baroLatestAltitude;
    // Serial.println("Estimated altitude: " + String(alt_est));
    // Serial.println("Estimated Velocity: " + String(vel_est));
    Serial.println("Barometer altitude: " + String(bara_alt));
  }
}
