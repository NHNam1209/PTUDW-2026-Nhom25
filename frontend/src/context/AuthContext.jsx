import React, { createContext, useContext, useState, useEffect } from 'react';
import { api } from '../api/client';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(() => {
    const saved = localStorage.getItem('user');
    return saved ? JSON.parse(saved) : null;
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchMe = async () => {
      if (api.accessToken) {
        try {
          const profile = await api.get('/auth/me');
          setUser(profile);
          localStorage.setItem('user', JSON.stringify(profile));
        } catch (err) {
          api.clearTokens();
          setUser(null);
        }
      }
      setLoading(false);
    };
    fetchMe();
  }, []);

  const login = async (email, password) => {
    const data = await api.post('/auth/login', { email, password });
    api.setTokens(data.accessToken, data.refreshToken);
    setUser(data.user);
    localStorage.setItem('user', JSON.stringify(data.user));
    return data.user;
  };

  const register = async (fullName, email, userName, password) => {
    const data = await api.post('/auth/register', {
      fullName,
      email,
      userName,
      password,
    });
    api.setTokens(data.accessToken, data.refreshToken);
    setUser(data.user);
    localStorage.setItem('user', JSON.stringify(data.user));
    return data.user;
  };

  const logout = async () => {
    try {
      if (api.refreshToken) {
        await api.post('/auth/logout', { refreshToken: api.refreshToken });
      }
    } catch (e) {
      // ignore logout errors
    } finally {
      api.clearTokens();
      setUser(null);
    }
  };

  const updateProfile = async (updateData) => {
    const updated = await api.patch('/auth/me', updateData);
    setUser(updated);
    localStorage.setItem('user', JSON.stringify(updated));
    return updated;
  };

  const isAuthenticated = !!user;
  const isAdmin = user?.roles?.includes('Admin');
  const isAuthor = user?.roles?.includes('Author') || isAdmin;

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        isAuthenticated,
        isAdmin,
        isAuthor,
        login,
        register,
        logout,
        updateProfile,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
