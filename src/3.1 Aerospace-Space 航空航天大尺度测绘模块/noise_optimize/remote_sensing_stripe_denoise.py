"""
遥感影像条带噪声抑制模块（场景专属）
底层依赖：Common-LSG constraint_algo 平滑算子
功能：去除卫星影像条带噪声、辐射不均，提升重建连续性
"""
from Common_LSG.constraint_algo import AdaptiveSmoother

class RemoteSensingDenoise(AdaptiveSmoother):
    def stripe_noise_remove(self, section_matrix, direction="horizontal"):
        """条带噪声自适应去除"""
        denoised_matrix = self.periodic_stripe_filter(section_matrix, direction=direction)
        return denoised_matrix

    def radiation_uniform_correct(self, section_stack):
        """辐射亮度均匀化校正"""
        corrected_stack = self.global_gray_equalize(section_stack)
        return corrected_stack