using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GetInt : MonoBehaviour {

	// Use this for initialization
	public GameObject input1;
	void Start () {
		InputField iField = input1.GetComponent<InputField>();
		iField.characterValidation = InputField.CharacterValidation.Integer;

	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
