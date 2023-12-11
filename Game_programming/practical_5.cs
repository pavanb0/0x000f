using UnityEngine;
using System.Collections;
public class Parralax : MonoBehaviour
{
    public float speed = 0.5f; // Adjust the speed as needed

    // Start is called before the first frame update
    void Start()
    {
        // Code that runs once at the start
    }

    // Update is called once per frame
    void Update()
    {
        // Calculate the offset based on time and speed
        Vector2 offset = new Vector2(Time.time * speed, 0);
        
        // Apply the offset to the material's mainTextureOffset
       GetComponent<Renderer>().material.mainTextureOffset = offset;
    }
}
