using UnityEngine;
using System.Collections;

public class ExampleClass : MonoBehaviour
{
    public Color color1 = Color.white;
   
    public Camera cam;

    void Start()
    {
        cam = GetComponent<Camera>();
        cam.clearFlags = CameraClearFlags.SolidColor;
    }

    void Update()
    {
        cam.backgroundColor = color1;
    }
}