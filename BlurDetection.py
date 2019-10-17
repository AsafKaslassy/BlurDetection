"""
:Description: This  Script computes the Laplacian of the image and then return the focus
              measure, which is the variance (standard deviation squared) of
              The Laplacian kernel. [3X3]
                  [  0   1    0  ]
                  [  1  -4    1  ]
                  [  0   1    0  ]

USAGE : blurDetection.exe BlurDetectionConfig.ini
"""

import os
import cv2
import time
import glob
import argparse
from configReader import read_config

start = time.time()


def variance_of_laplacian(image, save_path=None):
    """
    :Description: computes the Laplacian of the image and then return the focus
                  measure, which is the variance (standard deviation squared) of
                  The Laplacian kernel. [3X3]
                      [  0   1    0  ]
                      [  1  -4    1  ]
                      [  0   1    0  ]
    """

    lap_image = cv2.Laplacian(image, cv2.CV_64F)
    if save_path:
        cv2.imwrite(save_path, lap_image)
    return lap_image.var()


def run(ini_path):
    func_name = "Blur Detector"
    config = read_config(ini_path)
    vis_input = config["Vis input"]
    thresh = config["Threshold"]
    blur_score_txt_path = config["Blur Score txt path"]
    debug = config["Debug mode"]
    output_path = config["Output path"]
    output_edge = config["Output edge path"]
    log = Logger(config["Logger path"], func_name)

    # loop over the input images
    i = 1
    log.info("\n")
    log.info(' | Vis tested : "{}"'.format(vis_input))
    log.info(" | Threshold  : {}            \n".format(thresh))

    paths = glob.glob(os.path.join(vis_input, "*.jp*"))
    with open(os.path.join(blur_score_txt_path, "blur_score_txt.txt"), 'a') as f:
        f.write("\n _________________________________________________________________________________")
        f.write('\n | Vis tested : "{}"  \n'.format(vis_input))
        f.write(" | Threshold : {}            \n".format(thresh))
        f.write(" | Camera Number |      Blur score          |   Blurry or not      \n")
        f.write("  _________________________________________________________________________________\n")

    for imagePath in paths:
        # load the image, convert it to gray scale, and computes the Variance of Laplacian
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if not debug:
            var_of_lap = variance_of_laplacian(gray)
        else:
            var_of_lap = variance_of_laplacian(gray, os.path.join(output_edge, "%04d.jpg" % i))
        text = "Not Blurry"
        # if the focus measure is less than the supplied threshold,
        # then the image should be considered "blurry"
        with open(os.path.join(blur_score_txt_path, "blur_score_txt2.txt"), 'a') as f:

            if i < 10:
                if var_of_lap < thresh:
                    text = "Blurry"
                    f.write(" |   Camera {}    |  Blur Score: {:.3f}      |  {}\n".format(i, var_of_lap, text))
                else:
                    f.write(" |   Camera {}    |  Blur Score: {:.3f}      |  {}\n".format(i, var_of_lap, text))
            else:
                if var_of_lap < thresh:
                    text = "Blurry"
                    f.write(" |   Camera {}   |  Blur Score: {:.3f}      |  {}\n".format(i, var_of_lap, text))
                else:
                    f.write(" |   Camera {}   |  Blur Score: {:.3f}      |  {}\n".format(i, var_of_lap, text))

        if var_of_lap < thresh:
            text = "Blurry"
            log.info("| Camera {} is {}        Blur Score: {:.3f}".format(i, text, var_of_lap))
        else:
            log.info("| Camera {} is {}    Blur Score: {:.3f}".format(i, text, var_of_lap))
        if debug == 1:
            cv2.putText(image, "Camera {} is {} ,   Blur Score: {:.3f}".format(i, text, var_of_lap), (160, 160),
                        cv2.FONT_HERSHEY_SIMPLEX, 3.5, (255, 0, 255), 15)
            cv2.imwrite(os.path.join(output_path, "%04d.jpg" % i), image)
        i += 1

    end = time.time()
    log.info("| ________________________________________________________")
    log.info("|  Finished Successfully  |   Total time : {:.2f} Seconds  |\n\n\n".format(end-start))

# TODO: all values into a list and sort by score.
#     top_3_minimum_scores = min()
#     log.info(" Top 3 minimum blur scores: ")
#     log.info("Camera{},Blur Score:{}\n
#               Camera{},Blur Score:{}\n
#               Camera{},Blur Score:{}".format(cam[j],var_of_lap[j],
#                                              cam[k],var_of_lap[k],
#                                              cam[l],var_of_lap[l]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=__doc__)
    parser.add_argument("config_file_path", metavar="<ini_file>", type=str, help=" Path to .ini file needed")

args = parser.parse_args()
run(args.config_file_path)
