import os,sys

def main():
    
    fileNames = {1:['HelloWorldExample','DrawingShapesandColors','DisplayingImages','UsingGUIComponents','LayoutManagers'],
                 2:['ActionListener','MouseListener','MouseMotionListener'],
                 3:['StatusBarMessages','OpeningWebPages','PlayingSounds','UsingParameters'],
                 4:['DoubleBuffering','Threads','UsingLibraries'] }


    titleName = {'HelloWorldExample':'Hello World Example Applet',
                 'DrawingShapesandColors':'Drawing Shapes and Colors Applet',
                 'DisplayingImages':'Displaying Images Applet',
                 'UsingGUIComponents':'Using GUI Components Applet',
                 'LayoutManagers':'Layout Managers Applet',
                 'ActionListener':'Action Listener Applet',
                 'MouseListener':'Mouse Listener Applet',
                 'MouseMotionListener':'Mouse Motion Listener Applet',
                 'StatusBarMessages':'Status Bar Messages Applet',
                 'OpeningWebPages':'Opening Web Pages Applet',
                 'PlayingSounds':'Playing Sounds Applet',
                 'UsingParameters':'Using Parameters Applet',
                 'DoubleBuffering':'Double Buffering Applet',
                 'Threads':'Threads Applet',
                 'UsingLibraries':'Using Libraries Applet' }
    

    
    fileSuffix ='.html'
    filePrefix =''

    for i in range(4):
        for name in fileNames[i+1]:
            f = open(filePrefix+name+fileSuffix,'w')
            
            f.write('<!DOCTYPE html>\n')
            f.write('<html>\n<head>\n<title>'+titleName[name]+'</title>\n</head>\n')
            f.write('<body>\n\n\n')
            f.write('<center><a href=\"Chapter%s.html\">Return to Chapter %s</a></center>\n' % (i+1,i+1));
            f.write('</body>\n</html>\n')
            f.close()


if __name__ == "__main__":
    main()


















         
