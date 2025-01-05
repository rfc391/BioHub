
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def extract_features(data, n_components=2):
    """ Apply PCA to reduce dimensions of the dataset."""
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(scaled_data)
    return principal_components
