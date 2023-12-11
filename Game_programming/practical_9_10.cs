#PLAYER MOVE
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class player : MonoBehaviour
{
    public float moveSpeed = 5f;
    void Update()
    {
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");
 
        Vector3 movement = new Vector3(verticalInput, horizontalInput, 0) * moveSpeed *
        Time.deltaTime;
        transform.Translate(movement);
    }
}
 

#ENEMY MOVE
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
 
public class enemy : MonoBehaviour
{
    public string playerTag = "player";
    public float moveSpeed = 3.0f;
    private Transform playerTransform;
    void Start()
    {
        GameObject playerObject = GameObject.FindGameObjectWithTag(playerTag);
 
        if (playerObject != null)
        {
            playerTransform = playerObject.transform;
        }
        else
        {
 
            Debug.LogError("Player not found with tag: " + playerTag);
        }
    }
    void Update()
    {
        if (playerTransform != null)
        {
            Vector3 directionToPlayer = playerTransform.position - transform.position;
            directionToPlayer.Normalize();
            transform.position += directionToPlayer * moveSpeed * Time.deltaTime;
        }
        else
        {
            Debug.LogWarning("Player transform is null. Ensure the player has the correct tag.");
        }
    }
}
 
