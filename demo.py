from code.plot import contrast_plot,demo_viper_with_retinex
from code.retinex import retinex_FM,retinex_SSR,retinex_MSR,retinex_MSRCR,retinex_gimp,retinex_MSRCP,retinex_AMSR
from code.tools import cv2_heq, measure_time
import os.path
import cv2

img_dir=os.path.normpath(os.path.join(os.path.dirname(__file__),'./imgs'))
img=cv2.imread(os.path.join(img_dir,'demo2.png'))

#test1
#demo_viper_with_retinex(os.path.join(img_dir,'VIPeR.v1.0'),retinex_AMSR)

functions = [retinex_SSR, retinex_SSR, retinex_SSR, retinex_MSR, retinex_gimp, retinex_MSRCR, retinex_MSRCP, retinex_FM, cv2_heq, retinex_AMSR]
func_params = [[15], [80], [250], [], [], [], [], [], [], []]
func_labels = ['src', 'SSR(15)', 'SSR(80)', 'SSR(250)', 'MSR(15,80,250,0.333)', 'Gimp', 'MSRCR', 'MSRCP', 'FM', 'cv2 heq', 'Auto MSR']
func_outputs = []

for i in range(len(functions)):
    func_outputs.append(measure_time(functions[i], img, *func_params[i]))
    
#test2
contrast_plot(img, func_outputs,func_labels,save=False)