/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 3.0.10
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package io.thp.psmove;

public class _PSMove_3AxisVector {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected _PSMove_3AxisVector(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(_PSMove_3AxisVector obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        psmoveapiJNI.delete__PSMove_3AxisVector(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public void setX(float value) {
    psmoveapiJNI._PSMove_3AxisVector_x_set(swigCPtr, this, value);
  }

  public float getX() {
    return psmoveapiJNI._PSMove_3AxisVector_x_get(swigCPtr, this);
  }

  public void setY(float value) {
    psmoveapiJNI._PSMove_3AxisVector_y_set(swigCPtr, this, value);
  }

  public float getY() {
    return psmoveapiJNI._PSMove_3AxisVector_y_get(swigCPtr, this);
  }

  public void setZ(float value) {
    psmoveapiJNI._PSMove_3AxisVector_z_set(swigCPtr, this, value);
  }

  public float getZ() {
    return psmoveapiJNI._PSMove_3AxisVector_z_get(swigCPtr, this);
  }

  public void setV(SWIGTYPE_p_float value) {
    psmoveapiJNI._PSMove_3AxisVector_v_set(swigCPtr, this, SWIGTYPE_p_float.getCPtr(value));
  }

  public SWIGTYPE_p_float getV() {
    long cPtr = psmoveapiJNI._PSMove_3AxisVector_v_get(swigCPtr, this);
    return (cPtr == 0) ? null : new SWIGTYPE_p_float(cPtr, false);
  }

  public _PSMove_3AxisVector() {
    this(psmoveapiJNI.new__PSMove_3AxisVector(), true);
  }

}
