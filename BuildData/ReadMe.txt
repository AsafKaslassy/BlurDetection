Blur Detection 1.0.0.0:

	This  Script computes the Laplacian of the image and then return the focus
              measure, which is the variance (standard deviation squared) of
              The Laplacian kernel. [3X3]
                  [  0   1    0  ]
                  [  1  -4    1  ]
                  [  0   1    0  ]
	Outputs are:
		- txt file containing Blur Score for each camera.
		- log file.
		- Debug outputs Laplacian Edge Masks and Vis with Text indicating score and whether blurry or not
		
Configuration paramaters:

    [config.ini] - Version 1.0.0.0
    Vis input - Path to the images you'd like to test focus, for better results,
				make sure vis is masked with blurred edges (like for stabilizer's input)
    Threshold - Threshold given (per sport) for the decision of Blurry \ Sharp
	Calibration Path - Path to folder containing projection matrices in txt files and calibration.ma file (Full Resolution)
	
    [Debug]:
	Debug Mode - If 'Debug Mode' is one outputs will be generated in output Paths 
	
	Blur Score txt path - Path to where the images you'd like to test focus

	Output path - Path to the Vis with blur score printed on mainly for debugging

	Output edge path - Path to the laplacian edges images mainly for debugging

	Logger path - Path to save logger info
