import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider
import openseespy.opensees as ops


def recordFiberResponse(OutputName,eleNumber, sectionNumber):
    
    eleNumber = int(eleNumber)
    sectionNumber = int(sectionNumber)
    ops.recorder('Element' , '-file', 'Fiber.out', '-time', '-ele', eleNumber, 'section', str(sectionNumber), 'fiberData')



def plotFiberResponse(FiberName, LoadStep):
    
    fiberData  = np.loadtxt(FiberName,delimiter=' ')
    fiberYPosition = fiberData[:,1::5]
    fiberStress = fiberData[:,4::5]
    
    fig, = plt.plot(fiberYPosition[LoadStep,:], fiberStress[LoadStep,:])
    
    pass
    
    
def animateFiber2D(fiberYPosition, fiberResponse, skipStart = 0, skipEnd = 0, rFactor=1, 
           outputFrames=0, fps = 24, Xbound = [],Ybound = []):
    """
    Parameters
    ----------
    xinput : 1d array
        The input x coordinants. 
    yinput : 1d array
        The input y coordinants. 
    skipStart : int, optional
        If specified, this many datapoints will be skipped from the data start.
        The default is 0.
    skipEnd : int, optional
        If specified, this many frames will be skipped at the end of 
        the analysis. The default is 0.
    rFactor : int, optional
        If specified, only every "x" frames will be reduced by this factor. 
        The default is 1.
    outputFrames : int, optional
        The number of frames to be included after all other reductions. If the
        reduced number of frames is less than this value, no change is made.
        The default is 0.
    fps : int, optional
        Number of animation frames to be displayed per second. The default is 24.
    Xbound : [xmin, xmax], optional
        The domain of the chart. The default is 1.1 the max and min values.
    Ybound : [ymin, ymax], optional
        The range of the chart. The default is 1.1 the max and min values.

    
    """

    # Check if the x and y data are of the same length, if not raise a error.
    if len(fiberYPosition) != len(fiberResponse):
        raise Exception('Lengths of input vectors unequal')
    
    # If end data is not being skipped, use the full vector length.
    if skipEnd ==0:
        skipEnd = len(fiberYPosition)
    
    
    # Set up bounds based on data from 
    if Xbound == []:
        xmin = 1.1*np.min(fiberYPosition)
        xmax = 1.1*np.max(fiberYPosition)
    else:
        xmin = Xbound[0]       
        xmax = Xbound[1]
    
    if Ybound == []:
        ymin = 1.1*np.min(fiberResponse)  
        ymax = 1.1*np.max(fiberResponse)        
    else:
        ymin = Ybound[0]       
        ymax = Ybound[1]          
    
    
    # Remove unecessary data
    xinputs = fiberYPosition[skipStart:skipEnd, :]
    yinputs = fiberResponse[skipStart:skipEnd, :]

    # Reduce the data if the user specifies
    if rFactor != 1:
        xinputs = xinputs[::rFactor, :]
        yinputs = yinputs[::rFactor, :]
    
    # If the Frames isn't specified, use the length of the reduced vector.
    if outputFrames == 0:
        outputFrames = len(xinputs[:, 0])
    else:
        outputFrames = min(outputFrames,len(xinputs[:, 0]))
    
    # Get the final output frames. X doesn't change
    xinputs = xinputs[:outputFrames, :]
    yinputs = yinputs[:outputFrames, :]    
    xinput = xinputs[0,:]
    
    # Initialize the plot
    fig, ax = plt.subplots()
    line, = ax.plot(xinput, yinputs[0,:])
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    print(xmin)
    
    Frames = np.arange(0, outputFrames)
    FrameStart = int(Frames[0])
    FrameEnd = int(Frames[-1])
    
    # Slider Location and size relative to plot
    # [x, y, xsize, ysize]
    axSlider = plt.axes([0.25, .03, 0.50, 0.02])
    plotSlider = Slider(axSlider, 'Frame', FrameStart, FrameEnd, valinit=FrameStart, valfmt = '%d')
    
    # Animation controls
    global is_manual
    is_manual = False # True if user has taken control of the animation   
    
    def on_click(event):
        # Check where the click happened
        (xm,ym),(xM,yM) = plotSlider.label.clipbox.get_points()
        if xm < event.x < xM and ym < event.y < yM:
            # Event happened within the slider, ignore since it is handled in update_slider
            return
        else:
            # user clicked somewhere else on canvas = unpause
            global is_manual
            is_manual=False        
    
    # Define the update function
    # def update_line(time, xinput, yinputs, line):
    def update_line_slider(time):
        global is_manual
        is_manual=True

        time = int(time)
        # Get the current data        
        y = yinputs[time,:]
        
        # Update the background line
        line.set_data(xinput, y)
        
        fig.canvas.draw_idle()    
        
        return line,
    
    
    def update_plot(ii):
    
        # If the control is manual, we don't change the plot    
        global is_manual
        if is_manual:
            return line,
       
        # Find the close timeStep and plot that
        CurrentFrame = int(np.floor(plotSlider.val))
        CurrentFrame += 1
        if CurrentFrame >= FrameEnd:
            CurrentFrame = 0
        
        # Update the slider
        plotSlider.set_val(CurrentFrame)
        is_manual = False # the above line called update_slider, so we need to reset this
        return line,  
    
    
    plotSlider.on_changed(update_line_slider)
    
    # assign click control
    fig.canvas.mpl_connect('button_press_event', on_click)    
    
    interval = 1000/fps
    
    line_ani = animation.FuncAnimation(fig, update_plot, outputFrames, 
                                       # fargs=(xinput, yinputs, line), 
                                       interval=interval)
    return line_ani


def animateFiber2DFile(fiberFileName, skipStart = 0, skipEnd = 0, rFactor=1, 
           outputFrames=0, fps = 24, Xbound = [],Ybound = []):
    """
    Parameters
    ----------
    xinput : 1d array
        The input x coordinants. 
    yinput : 1d array
        The input y coordinants. 
    skipStart : int, optional
        If specified, this many datapoints will be skipped from the data start.
        The default is 0.
    skipEnd : int, optional
        If specified, this many frames will be skipped at the end of 
        the analysis. The default is 0.
    rFactor : int, optional
        If specified, only every "x" frames will be reduced by this factor. 
        The default is 1.
    outputFrames : int, optional
        The number of frames to be included after all other reductions. If the
        reduced number of frames is less than this value, no change is made.
        The default is 0.
    fps : int, optional
        Number of animation frames to be displayed per second. The default is 24.
    Xbound : [xmin, xmax], optional
        The domain of the chart. The default is 1.1 the max and min values.
    Ybound : [ymin, ymax], optional
        The range of the chart. The default is 1.1 the max and min values.

    """    
    
    
    fiberData  = np.loadtxt(fiberFileName,delimiter=' ')
    fiberYPosition = fiberData[:,1::5]
    fiberStress = fiberData[:,4::5]    
    
    ani = animateFiber2D(fiberYPosition, fiberStress, skipStart, skipEnd, rFactor, outputFrames, fps, Xbound, Ybound)
    
    return ani