/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 3.0.10
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package io.thp.psmove;

public enum ConnectionType {
  Conn_Bluetooth,
  Conn_USB,
  Conn_Unknown;

  public final int swigValue() {
    return swigValue;
  }

  public static ConnectionType swigToEnum(int swigValue) {
    ConnectionType[] swigValues = ConnectionType.class.getEnumConstants();
    if (swigValue < swigValues.length && swigValue >= 0 && swigValues[swigValue].swigValue == swigValue)
      return swigValues[swigValue];
    for (ConnectionType swigEnum : swigValues)
      if (swigEnum.swigValue == swigValue)
        return swigEnum;
    throw new IllegalArgumentException("No enum " + ConnectionType.class + " with value " + swigValue);
  }

  @SuppressWarnings("unused")
  private ConnectionType() {
    this.swigValue = SwigNext.next++;
  }

  @SuppressWarnings("unused")
  private ConnectionType(int swigValue) {
    this.swigValue = swigValue;
    SwigNext.next = swigValue+1;
  }

  @SuppressWarnings("unused")
  private ConnectionType(ConnectionType swigEnum) {
    this.swigValue = swigEnum.swigValue;
    SwigNext.next = this.swigValue+1;
  }

  private final int swigValue;

  private static class SwigNext {
    private static int next = 0;
  }
}

