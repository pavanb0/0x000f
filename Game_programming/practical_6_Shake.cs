using System.Collections;
using UnityEngine;

public class SHAKE_THE_CAM : MonoBehaviour
{
    public float shakeDuration = 0.5f;
    public float shakeIntensity = 0.1f;

    private Vector3 originalPosition;

    void Start()
    {
        originalPosition = transform.localPosition;
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))  // You can trigger the shake using any condition you like
        {
            StartCoroutine(Shake());
        }
    }

    IEnumerator Shake()
    {
        float elapsedTime = 0f;

        while (elapsedTime < shakeDuration)
        {
            Vector3 randomOffset = Random.insideUnitSphere * shakeIntensity;
            transform.localPosition = originalPosition + randomOffset;

            elapsedTime += Time.deltaTime;

            yield return null;
        }

        transform.localPosition = originalPosition;  // Reset to original position after the shake
    }
}
