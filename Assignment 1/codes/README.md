
### Initial Approach: 5x5 Edge Interpolation Algorithm
We initially implemented a **5x5 edge-aware interpolation algorithm** for the **demosaicing** stage. This algorithm uses a 5x5 kernel to interpolate missing color values based on edge direction and intensity gradients in the raw image.

#### Issues Encountered:
- The algorithm produced suboptimal results in preserving edge details for complex patterns and textures and produced sub par image with very low brightness even after gamma implementation.
- Significant artifacts, such as zippering and color fringing, were observed around high-contrast edges.
  
#### Benefits of OpenCV's inbuilt demosaicing algorithm using Linear Interpolation:
- Faster and computationally efficient for large datasets.
- Provides acceptable quality for most general-use cases.
- Seamlessly integrates with the pipeline, ensuring smooth image transitions between stages.

#### Trade-offs:
- While linear interpolation lacks the edge-awareness of advanced algorithms, it strikes a balance between quality and performance, making it suitable for this application.
