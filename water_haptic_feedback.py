'''
This file is a stub for what the haptic feedback for
switching to "Water" mode on the AppleWatch would look like.
I made a swift implementation that is commented, so if I
ever had acess to Apple hardware I could easily port it
'''

def water_haptic_feedback():
    print(
        '''
        import WatchKit
        // Import everything else I would need for the project
        
        class InterfaceController: WKInterfaceController
        {
            override func awake(withContext context: Any?) 
            {
                super.awake(withContext: context)
                activateWaterMode()
            }

            func activateWaterMode() 
            {
                // Flat intensity
                WKInterfaceDevice.current().play(.start)
                // Ramp up to full intensity (I unfortunately think this will be linear)
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) 
                {
                    WKInterfaceDevice.current().play(.click)
                }
                // Gradually go to zero
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) 
                {
                    WKInterfaceDevice.current().play(.stop)
                }
            }
        }
        '''
    )