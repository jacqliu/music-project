//------------------------------------------------------------------------------
// <auto-generated />
//
// This file was automatically generated by SWIG (http://www.swig.org).
// Version 3.0.10
//
// Do not make changes to this file unless you know what you are doing--modify
// the SWIG interface file instead.
//------------------------------------------------------------------------------

namespace io.thp.psmove {

public class _PSMove_3AxisVector : global::System.IDisposable {
  private global::System.Runtime.InteropServices.HandleRef swigCPtr;
  protected bool swigCMemOwn;

  internal _PSMove_3AxisVector(global::System.IntPtr cPtr, bool cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = new global::System.Runtime.InteropServices.HandleRef(this, cPtr);
  }

  internal static global::System.Runtime.InteropServices.HandleRef getCPtr(_PSMove_3AxisVector obj) {
    return (obj == null) ? new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero) : obj.swigCPtr;
  }

  ~_PSMove_3AxisVector() {
    Dispose();
  }

  public virtual void Dispose() {
    lock(this) {
      if (swigCPtr.Handle != global::System.IntPtr.Zero) {
        if (swigCMemOwn) {
          swigCMemOwn = false;
          psmoveapi_csharpPINVOKE.delete__PSMove_3AxisVector(swigCPtr);
        }
        swigCPtr = new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero);
      }
      global::System.GC.SuppressFinalize(this);
    }
  }

  public float x {
    set {
      psmoveapi_csharpPINVOKE._PSMove_3AxisVector_x_set(swigCPtr, value);
    } 
    get {
      float ret = psmoveapi_csharpPINVOKE._PSMove_3AxisVector_x_get(swigCPtr);
      return ret;
    } 
  }

  public float y {
    set {
      psmoveapi_csharpPINVOKE._PSMove_3AxisVector_y_set(swigCPtr, value);
    } 
    get {
      float ret = psmoveapi_csharpPINVOKE._PSMove_3AxisVector_y_get(swigCPtr);
      return ret;
    } 
  }

  public float z {
    set {
      psmoveapi_csharpPINVOKE._PSMove_3AxisVector_z_set(swigCPtr, value);
    } 
    get {
      float ret = psmoveapi_csharpPINVOKE._PSMove_3AxisVector_z_get(swigCPtr);
      return ret;
    } 
  }

  public SWIGTYPE_p_float v {
    set {
      psmoveapi_csharpPINVOKE._PSMove_3AxisVector_v_set(swigCPtr, SWIGTYPE_p_float.getCPtr(value));
    } 
    get {
      global::System.IntPtr cPtr = psmoveapi_csharpPINVOKE._PSMove_3AxisVector_v_get(swigCPtr);
      SWIGTYPE_p_float ret = (cPtr == global::System.IntPtr.Zero) ? null : new SWIGTYPE_p_float(cPtr, false);
      return ret;
    } 
  }

  public _PSMove_3AxisVector() : this(psmoveapi_csharpPINVOKE.new__PSMove_3AxisVector(), true) {
  }

}

}
