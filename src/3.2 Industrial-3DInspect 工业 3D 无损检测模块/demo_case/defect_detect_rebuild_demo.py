"""
工业缺陷三维检测重建Demo
"""
from Industrial_3DInspect.hardware_adapt.industrial_ct_parser import IndustrialCTParser
from Industrial_3DInspect.noise_optimize.industrial_ct_artifact_optimize import IndustrialCTArtifactOptimize
from Industrial_3DInspect.scene_constraint.defect_boundary_constraint import DefectBoundaryConstraint
from Common_LSG.slice_rebuild import SectionRebuilder

def defect_detect_pipeline(ct_folder, output_path):
    parser = IndustrialCTParser()
    ct_data = parser.load_industrial_ct_series(ct_folder)
    
    optimizer = IndustrialCTArtifactOptimize()
    optimized_stack = [optimizer.high_contrast_artifact_remove(s) for s in ct_data.section_stack]
    
    constraint = DefectBoundaryConstraint()
    constrained_stack = [constraint.micro_defect_enhance(s, defect_size_min=0.1) for s in optimized_stack]
    
    rebuilder = SectionRebuilder()
    defect_model = rebuilder.non_orthogonal_rebuild(constrained_stack, ct_data.spacing)
    
    print("工业工件缺陷三维重建完成，支持缺陷定量测量")
    return defect_model

if __name__ == "__main__":
    defect_detect_pipeline("./industrial_ct", "./output/defect_model.stl")