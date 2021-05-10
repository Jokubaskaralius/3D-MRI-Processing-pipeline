# Import data
import time
import typing
import nibabel as nib
import numpy as np
from skimage import io
import plotly.graph_objects as go
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
from matplotlib.colors import ListedColormap
from transforms import Resize

def frame_args(duration):
    return {
            "frame": {"duration": duration},
            "mode": "immediate",
            "fromcurrent": True,
            "transition": {"duration": duration, "easing": "linear"},
        }


def visualizeImage2D(vol_path: str, proc_vol_path: str):
    img_proc = nib.load(vol_path)
    img_unproc = nib.load(proc_vol_path)

    data_proc = img_proc.get_fdata()
    x_p,y_p,z_p = data_proc.shape

    data_unproc = img_unproc.get_fdata()
    x_u,y_u,z_u = data_unproc.shape

    slice_0_proc = data_proc[int(x_p/2), :, :]
    slice_1_proc = data_proc[:, int(y_p/2), :]
    slice_2_proc = data_proc[:, :, int(z_p/2)]

    slice_0_unproc = data_unproc[int(x_u/2), :, :]
    slice_1_unproc = data_unproc[:, int(y_u/2), :]
    slice_2_unproc = data_unproc[:, :, int(z_u/2)]

    f = show_slices([slice_0_proc, slice_1_proc, slice_2_proc])
    plt.suptitle("Center slices for unprocessed MRI image")
    plt.tight_layout(pad=2.0)

    move_figure(f, 830, 83)

    f_p = show_slices([slice_0_unproc, slice_1_unproc, slice_2_unproc])
    plt.suptitle("Center slices for processed MRI image")
    plt.tight_layout(pad=2.0)
    move_figure(f_p, 0, 83)
    plt.show()


def visualizeImage3D(vol_path: str, proc_vol_path: str):
    img_proc = nib.load(proc_vol_path)
    img_unproc = nib.load(vol_path)

    data_proc = img_proc.get_fdata()
    data_unproc = img_unproc.get_fdata()
    
    
    resize_proc = Resize((data_proc, img_proc.affine, img_proc.header), (50,50,26))
    resize_unproc = Resize((data_unproc, img_unproc.affine, img_unproc.header), (50,50,26))

    data_proc = resize_proc()
    data_unproc = resize_unproc()

    x_p = []
    y_p = []
    z_p = []
    c_p = []
    x = []
    y = []
    z = []
    c = []

    for sur in range(data_proc.shape[0]):
        for row in range(data_proc.shape[1]):
            for col in range(data_proc.shape[2]):
                x_p.append(sur)
                y_p.append(row)
                z_p.append(col)
                c_p.append(data_proc[sur][row][col])

    for sur in range(data_unproc.shape[0]):
        for row in range(data_unproc.shape[1]):
            for col in range(data_unproc.shape[2]):
                x.append(sur)
                y.append(row)
                z.append(col)
                c.append(data_unproc[sur][row][col])

    fig_proc = plt.figure()
    plt.suptitle("3D MRI processed MRI image")
    fig_unproc = plt.figure()
    plt.suptitle("3D MRI unprocessed MRI image")
    ax_proc = fig_proc.add_subplot(111, projection='3d')
    ax_unproc = fig_unproc.add_subplot(111, projection='3d')

    # Choose colormap
    cmap = pl.cm.RdBu

    # Get the colormap colors
    my_cmap = cmap(np.arange(cmap.N))

    # Set alpha
    my_cmap[:, -1] = np.linspace(0, 1, cmap.N)

    # Create new colormap
    my_cmap = ListedColormap(my_cmap)

    fig_p = ax_proc.scatter(x_p, y_p, z_p, c=c_p, cmap=my_cmap)
    fig_u = ax_unproc.scatter(x, y, z, c=c, cmap=my_cmap)
    
    fig_proc.colorbar(fig_p)
    fig_unproc.colorbar(fig_u)

    move_figure(fig_unproc, 830, 83)
    move_figure(fig_proc, 0, 83)

    plt.show()




def move_figure(f, x, y):
    """Move figure's upper left corner to pixel (x, y)"""
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    elif backend == 'WXAgg':
        f.canvas.manager.window.SetPosition((x, y))
    else:
        # This works for QT and GTK
        # You can also use window.setGeometry
        f.canvas.manager.window.move(x, y)

def show_slices(slices):
    #Function to display row of image slices
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")
        axes[i].set_xlabel('element')
        axes[i].set_ylabel('element')

    return fig
