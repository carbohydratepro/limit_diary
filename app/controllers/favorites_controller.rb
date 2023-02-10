class FavoritesController < ApplicationController
  def create
    blog = blog.find(params[:blog_id])
    favorite = current_user.favorites.new(blog_id: blog.id)
    favorite.save
    redirect_to request.referer
  end

  def destroy
    blog = blog.find(params[:blog_id])
    favorite = current_user.favorites.find_by(blog_id: blog.id)
    favorite.destroy
    redirect_to request.referer
  end

end
