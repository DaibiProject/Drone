void mspCom() {
  // msp_attitude_t attitude;
  msp_raw_imu_t imu; 
  msp_altitude_t altitude;
  
  msp.command(MSP_SET_RAW_RC, &rc, sizeof(rc), true);
  
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
    int32_t bara_alt = altitude.baroLatestAltitude;
    Serial.println("Barometer altitude: " + String(bara_alt));
  }
}
