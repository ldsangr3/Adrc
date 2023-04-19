    # Apply Butterworth filter
filtered_lvl_PBR3 = self.apply_butterworth_filter(self.lvl_PBR3)
        
self.wFBR3.xLvl.plot(self.Timelvl_PBR3,filtered_lvl_PBR3), self.wFBR3.xLvl.grid(True)  
self.wFBR3.lineLvl.draw()  
        
# Control_Nivel on/off simply
# First computed the average of the last elements of the vectors
last_third_PBR1 = filtered_lvl_PBR1[-(N//3):]
average_last_third_PBR1 = sum(last_third_PBR1) / len(last_third_PBR1)