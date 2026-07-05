永久记录本目录分层架构（本次给你的完整文件夹树）

2.1 Medical-CT 医学 CT 三维重建模块
Medical-CT/
├─ scene_constraint/
│  └─ ct_tissue_constraint.py
├─ noise_optimize/
│  └─ ct_artifact_removal.py
├─ hardware_adapt/
│  └─ dicom_ct_parser.py
├─ demo_case/
│  └─ ct_3d_rebuild_demo.py
└─ README.md
### 2.2 Medical-Ultrasound 超声成像三维重建模块
#### 目录结构
Medical-Ultrasound/
├─ scene_constraint/
│ └─ us_acoustic_constraint.py
├─ noise_optimize/
│ └─ us_speckle_denoise.py
├─ hardware_adapt/
│ └─ us_signal_parser.py
├─ demo_case/
│ └─ us_3d_rebuild_demo.py
└─ README.md
2.3 Geo-MountainNav 山区无人机离线导航模块
Geo-MountainNav/
├─ scene_constraint/
│  └─ terrain_gradient_constraint.py
├─ noise_optimize/
│  └─ pointcloud_outlier_clean.py
├─ hardware_adapt/
│  └─ lidar_vision_parser.py
├─ demo_case/
│  └─ mountain_nav_map_demo.py
└─ README.md
2.4 Ocean-SubNav 水下潜航海底测绘导航模块
Ocean-SubNav/
├─ scene_constraint/
│  └─ seabed_terrain_constraint.py
├─ noise_optimize/
│  └─ sonar_scatter_denoise.py
├─ hardware_adapt/
│  └─ multibeam_sonar_parser.py
├─ demo_case/
│  └─ seabed_rebuild_demo.py
└─ README.md